from sys import stdin
def LI(): return list(map(int,stdin.readline().rstrip().split()))

li = LI()

for i in range(len(li)):
    for j in range(i+1,len(li)):
        if li[i]+li[j] == li[3-i-j]:
            print('Yes')
            exit()

print('No')