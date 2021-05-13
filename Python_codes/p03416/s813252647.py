A,B = map(int,input().split())
List = [str(i) for i in range(A,B+1)]
count = 0
for i in List:
    if i == i[::-1]:
        count += 1
print(count)