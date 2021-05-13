n = int(input())
dic = {}
for i in range(n):
    a = input()
    if a[0] == "i":
        dic[a[7:]] = 0
    else:
        print("yes" if a[5:] in dic else "no")