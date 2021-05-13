s = input()
count = int(input())
li = ["print", "reverse", "replace"]
for i in range(count):
    exp= input().split()
    a = int(exp[1])
    b = int(exp[2])
    ind = li.index(exp[0])
    if ind == 0:
        print(s[int(a):int(b)+1])
    elif ind == 1:
        s = s[:a] + s[a:b+1][::-1] + s[b+1:]
    else:
        s = s[:a] + exp[3] + s[b+1:]