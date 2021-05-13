k = int(input())
a = list(map(int,input().split()))

upper,lower = 2,2

for ai in a[::-1]:
    lower = (1+(lower-1)//ai)*ai
    upper = (1 + upper//ai)*ai -1
    if(upper < lower):
        print(-1)
        exit()
    # print(lower,upper)

print(' '.join(map(str,[lower,upper])))