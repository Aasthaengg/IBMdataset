m500 = int(input())
m100 = int(input())
m50 = int(input())
X = int(input())

count = 0

for i in range(m500+1):
    for j in range(m100+1):
        for k in range(m50+1):
            if X == i*500+j*100+k*50:
                count += 1

print(count)