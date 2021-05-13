class place:

    def __init__(self, a):
        b = len(a)
        
        for i in range(len(a)):
            if(a[i] == 0):
                print(i + 1)
                break



a = list(map(int,input().split()))
place(a)

