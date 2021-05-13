def ii():return int(input())
def iim():return map(int,input().split())
def iil():return list(map(int,input().split()))
n = ii()
music = []
length = []
for i in range(n):
    ti,leng = map(str,input().split())
    music.append(ti)
    length.append(int(leng))
x = input()

num = music.index(x)
print(sum(length[num+1::]))