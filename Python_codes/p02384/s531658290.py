class Daise:
    def __init__(self, info_list):
        self.T = info_list[0]
        self.S = info_list[1]
        self.E = info_list[2]
        self.W = info_list[3]
        self.N = info_list[4]
        self.B = info_list[5]
    
    def change(self, axis):
        if axis == 'S':
            self.T, self.B, self.S, self.N = self.N, self.S, self.T, self.B
        
        elif axis == 'E':
            self.T, self.B, self.E, self.W = self.W, self.E, self.T, self.B
        
        elif axis == 'W':
            self.T, self.B, self.W, self.E = self.E, self.W, self.T, self.B
        
        elif axis == 'N':
            self.T, self.B, self.N, self.S = self.S, self.N, self.T, self.B
        
        elif axis == 'Turn':
            self.S, self.E, self.N, self.W = self.E, self.N, self.W, self.S


if __name__ == '__main__':
    info = list(map(str, input().split()))
    n_input = int(input())

    for _ in range(n_input):
        obj = Daise(info)
        operation = list(map(str, input().split()))
        
        if operation[1] in (obj.T, obj.B):
            obj.change("S")
            
        while obj.S != operation[1]:
            obj.change('Turn')

        while obj.T != operation[0]:
            obj.change('E')

        print(obj.E)
