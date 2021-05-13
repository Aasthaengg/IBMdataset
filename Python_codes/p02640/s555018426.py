flag = False
n, y = list(map(int, input().split()))
for i in range(0, n):
        if i*2 + (n-i) * 4 == y or i*4 + (n-i)*2 ==y:
            flag = True
            break

print("Yes") if flag else print("No")
