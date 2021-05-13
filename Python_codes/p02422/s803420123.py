class String:
    def __init__(self,letter):
        self.letter=letter
        self.memory=''
    def println(self,start,end):
        print(self.letter[start:(end+1)])
    def replace(self,start,end,alt):
        self.memory=''
#         obj=self.letter[start:(end+1)]
        if(start!=0 and end!=(len(self.letter)-1)):
            self.memory=self.letter[0:start]+alt+self.letter[(end+1):]
        elif(start==0):
            self.memory=alt+self.letter[(end+1):]
        elif(end==(len(self.letter)-1)):
            self.memory=self.letter[:start]+alt
        self.letter=self.memory
#         self.letter=self.letter.replace(obj,alt)
    def reverse(self,start,end):
        self.memory=''
        if(start==0):
            obj=self.letter[end::-1]
            self.memory=obj+self.letter[(end+1):]
        else:
            obj=self.letter[end:(start-1):-1]
            self.memory=self.letter[0:start]+obj+self.letter[(end+1):]
        self.letter=self.memory
    def check(self):
        return self.letter
    
##main##
val=input()
q=int(input())
my_str=String(val)
for i in range(q):
    command=input().split()
    if(command[0]=="print"):
        my_str.println(int(command[1]),int(command[2]))
    elif(command[0]=="replace"):
        my_str.replace(int(command[1]),int(command[2]),command[3])
    elif(command[0]=="reverse"):
        my_str.reverse(int(command[1]),int(command[2]))


