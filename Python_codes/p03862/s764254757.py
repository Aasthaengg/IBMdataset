n, border = map(int, input().split())

boxes = [int(x) for x in input().split(' ')]

count = 0
for  i in range(n):
    if(boxes[i] > border):
        count += boxes[i] - border
        boxes[i] = border

for i in range(n-1):
    if(boxes[i] + boxes[i+1] > border):
        count += boxes[i] + boxes[i+1] - border
        boxes[i+1] -= boxes[i] + boxes[i+1] - border
        
print(count)