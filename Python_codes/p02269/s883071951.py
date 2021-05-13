#define hash
class my_dict():
    def __init__(self, size=1000):
        self.my_list = [[] for i in range(size)]
        self.dict_size = size
    #quaternary A=0 C=1 G=2 T=3
    def acgt_hash(self, input_str):
        output = 0
        for i in input_str:
            if i == 'A':
                output+=1
            elif i == 'C':
                output+=2
            elif i == 'G':
                output+=3
            elif i == 'T':
                output+=4
            output *=5
        return output%self.dict_size
    def insert(self, key):
        hash_val = self.acgt_hash(key)
        if self.my_list[hash_val] == None:
            self.my_list[hash_val]  = [key]
        else:
            for k in self.my_list[hash_val]:
                if k == key:
                    break
            else: self.my_list[hash_val].append(key)
    def find(self, key):
        hash_val = self.acgt_hash(key)
        if self.my_list[hash_val] == None:
            print('no')
        else:
            for k in self.my_list[hash_val]:
                if k == key:
                    print('yes')
                    break
            else: print('no')

#get N
n = int(input())
#create dic
dic1 = my_dict(100000)
#get inputs in N times
for i in range(n):
    #get instructtion and key
    inst, key = input().split(' ')
    #do instructions
    if inst == 'insert':
        dic1.insert(key)
    else:
        dic1.find(key)



