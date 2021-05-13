X = int(input())

count = 0
temp = 100
ans = 0
while True:
    temp+=temp//100
    count += 1
    ans  = temp
    if ans>=X:
        break
print(count)