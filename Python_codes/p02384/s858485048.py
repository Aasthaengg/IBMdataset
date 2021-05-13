class Saikoro:

    def sai(self,one,two,three,four,five,six):
        self.s1=int(one)
        self.s2=int(two)
        self.s3=int(three)
        self.s4=int(four)
        self.s5=int(five)
        self.s6=int(six)

    def turnE(self):
        e=[self.s4,self.s2,self.s1,self.s6,self.s5,self.s3]
        self.s1=e[0]
        self.s2=e[1]
        self.s3=e[2]
        self.s4=e[3]
        self.s5=e[4]
        self.s6=e[5]

    def turnN(self):
        n=[self.s2,self.s6,self.s3,self.s4,self.s1,self.s5]
        self.s1=n[0]
        self.s2=n[1]
        self.s3=n[2]
        self.s4=n[3]
        self.s5=n[4]
        self.s6=n[5]


l=input().split()

sai1=Saikoro()
sai1.sai(l[0],l[1],l[2],l[3],l[4],l[5])

q=int(input())

i=0
Ans=[]
while i<q:
    m=input().split()
    ichi=int(m[0])
    ni=int(m[1])
    sai1.sai(l[0],l[1],l[2],l[3],l[4],l[5])
    p=0
    while p<4:
        if ichi==int(l[0]) and ni==int(l[2]) or ichi==int(l[2]) and ni==int(l[5]) or ichi==int(l[5]) and ni==int(l[3]) or ichi==int(l[3]) and ni==int(l[0]) :
            Ans.append(int(l[4]))
            break
        elif ichi==int(l[5]) and ni==int(l[2]) or ichi==int(l[2]) and ni==int(l[0]) or ichi==int(l[0]) and ni==int(l[3]) or ichi==int(l[3]) and ni==int(l[5]) :
            Ans.append(int(l[1]))
            break
        w=0
        sai1.turnE()
        while w<4:
            sai1.turnN()
            if sai1.s1==ichi and sai1.s2==ni:
                Ans.append(sai1.s3)
                break
            else:
                pass
            w+=1
        p+=1
    i+=1

for A in Ans:
    print(A)

