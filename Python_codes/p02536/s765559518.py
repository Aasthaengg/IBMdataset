class disjoint_set:
    def __init__(self,num):

        self.array=[0]+[[i,0] for i in range(1,num+1)]  # our set
    
    def union(self,a,b):
        
        ''' a and b are the vertices that we want to connect them to each other '''
        
        a=self.find(a) # finds the ancestor of a
        b=self.find(b) # finds the ancestor of b
    
        if a==b:
            # if the ancestors of a and b are the same , do nothing
            return False
    

        # connecting two graph components to each other

        if self.array[a][1] > self.array[b][1] :
            self.array[b][0]=a
        
        elif self.array[a][1] < self.array[b][1] :
            self.array[a][0]=b

        else:
            self.array[a][0]=b
            self.array[b][1]+=1
        return True
            
    def find(self,a):
        p=[]
        while self.array[a][0]!=a :
            p.append(a)
            a=self.array[a][0]
        for i in p:
            self.array[i][0]=a
        return a

##############################3
n,m=map(int,input().split())
dset=disjoint_set(n)
for _ in range(m):
    a,b=map(int,input().split())
    dset.union(a,b)

ans=set()
for i in range(1,n+1) :
    ans.add(dset.find(i))

print(len(ans)-1)