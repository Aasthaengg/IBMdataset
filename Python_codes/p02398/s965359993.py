count = 0
count = int(count)
a,b,c = map(int,input().split())
while a <= b:
    if c % a == 0 :
        count = count + 1
    a = a + 1       
print('{}'.format(count))