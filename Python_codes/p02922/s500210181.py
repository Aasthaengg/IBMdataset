#B - Power Socket
A,B = map(int,input().split())

count = 0
total_plug = 1
for i in range(1,B):
    count += 1
    total_plug += (A - 1)
    if B <= total_plug:
        break
        
print(count)
