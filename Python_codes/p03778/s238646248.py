w,a,b = map(int,(input().split()))

result = 0
if a < b :
    hantei = b - a - w
else:
    hantei = a - b - w 

for i in range(1,10**5):
    #print("hantei",hantei)
    if hantei <= 0:
        print(result)
        exit()
    else:
        hantei -= 1
        result += 1
