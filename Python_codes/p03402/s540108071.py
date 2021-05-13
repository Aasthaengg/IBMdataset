

a,b = [int(x) for x in input().split()]

a,b = a-1,b-1

H,W = 100,100


masu = [["." for i in range(100)] for _ in range(100)]
for h in range(100):
    for i in range(100):
        if i < 50:
            masu[h][i] = "#"

def white(masu):
    count = 0
    for i in range(500):
        for h in range(50):
            if a <= count:
                return masu
            count+=1
            masu[2*h][2*i] = "."
            

def black(masu):
    count = 0
    for i in range(500):
        for h in range(50):
            if b <= count:
                return masu
            count+=1
            masu[2*h][99 - 2*i] = "#"
            

def output(masu):
    for line in masu:
       print("".join(line))

print(str(H)+" "+str(W))

masu = white(masu)
masu = black(masu)
output(masu)