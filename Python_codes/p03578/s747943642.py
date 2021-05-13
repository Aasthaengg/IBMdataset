from collections import Counter
n = int(input())
D = Counter(map(int,input().split()))
m = int(input())
for i in map(int,input().split()):
    try:
        D[i] -= 1
        if D[i] < 0:
            print("NO")
            break
    except:
        print("NO")
        break
else:
    print("YES")