n = int(input())
s = input()

pin = []
cnt = 0

for i in range(0, 1000):
    pin.append(str(i).zfill(3))
#print(pin)

for i in range(0, 1000):
    k = 0
    for j in range(len(s)):
        if pin[i][k] == s[j]:
            k += 1
            if k == 3:
                cnt += 1
                break
                
print(cnt)