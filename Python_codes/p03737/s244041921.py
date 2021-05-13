a = list(map(str, input().split()))
b= [a[i][0]for i in range(3)]
c= [b[i].upper() for i in range(3)]
print("".join(c))