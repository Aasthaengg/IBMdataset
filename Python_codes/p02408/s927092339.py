cards_remain=[]
suit=["S","H","C","D"]
cards_set=[]
output=[]

count_card=input()

for l in range(int(count_card)):
        cards_remain.append(input())

for m in suit:
    for n in range(13):
        cards_set.append(m+" "+str(n+1))

for p in cards_set:
    if p not in  cards_remain:
        output.append(p)

for x in output:
        print(x)