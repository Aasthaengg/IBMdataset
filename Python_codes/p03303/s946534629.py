s = input()
w = int(input())
for i in range(len(s)//w+1):
    if i*w < len(s):
        print(s[i*w], end="")
print()