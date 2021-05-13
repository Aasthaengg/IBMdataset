arr=[int(input()) for i in range(5)]
k=int(input())

check="Yay!"
for i in range(4):
    for j in range(1,5-i):
       
        if arr[i+j]-arr[i]>k:
            check=":("
            break
    if check==":(":
        break
print(check)