n=int(input())

score=0

for i in range((n+1)//2):
    i=i*2+1
    yakusuu1 = []
    yakusuu2 = []
    d=1
    while d*d <= i:
        if i%d==0:
            yakusuu1.append(d)
            
            if d!= i//d: #べき乗ではなかったら　ex:2*2=4
                yakusuu2.append(i//d)
        
        d=d+1
    yakusuu = yakusuu1+yakusuu2[::-1]
    # print(i,yakusuu)
    
    if len(yakusuu) == 8:
        score = score+1
print(score)