st = input()
li = list(st)
an = abs(int(li[0]+li[1]+li[2]) - 753)
for i in range(1,len(li)-2):
    x = int(li[i]+li[i+1]+li[i+2])
    y = abs(x - 753)
    an = min(an,y)
print(an)