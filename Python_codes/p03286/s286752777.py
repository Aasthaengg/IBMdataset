N = int(input())
num = N
bit = []
for i in range(1,10000):
    r = abs(num%2)
    bit.append(str(r))
    num = (num-r)//-2
    if num == 0 :
        break
bit.reverse()
print(''.join(bit))