nums = list(map(int, input().split()))
cards = {'r':nums[0], 'g':nums[1], 'b':nums[2]}
tN = int(input())

def func_check():
    judge = 0
    if cards['g'] > cards['r']:
        judge += 1
    if cards['b'] > cards['g']:
        judge += 2
    if judge == 0:
        c = 'g'
    elif judge == 1:
        c = 'b'
    elif judge == 2:
        c = 'g'
    elif judge == 3:
        c = 'comp'
    return c

for i in range(tN):
    judge = func_check()
    if judge == 'comp':
        break
    else:
        cards[judge] *= 2
judge = func_check()
if judge == 'comp':
    output = 'Yes'
else:
    output = 'No'
print(output)
        
