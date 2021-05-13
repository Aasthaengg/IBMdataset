s=input()
kouho=set()
for i in range(2**4):
    word=list("AKIHABARA".replace("A","x"))# xの部分にAをいれるかいれないか
    if i&(1<<0):
        word[0]="A"
    if i&(1<<1):
        word[4]="A"
    if i&(1<<2):
        word[-3]="A"
    if i&(1<<3):
        word[-1]="A"
    k="".join(word)
    k=k.replace("x","")
    kouho.add(k)

if s in kouho:
    print('YES')
else:
    print('NO')
    
