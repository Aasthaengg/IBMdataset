num = int(raw_input())
a = map(int, raw_input().split())
Max = a[0]
Min = a[0]
Sum = 0
for i in range(num):
    if Max < a[i]:
        Max = a[i]
    if Min > a[i]:
        Min = a[i]
    Sum = Sum + a[i]
print "%d %d %d" %(Min, Max, Sum)