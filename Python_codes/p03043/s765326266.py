n, k = map(int,input().split())

dice_num = 1

def get_prob(dice_num,k):
    i = 0
    while True:
        i += 1
        if i ==1:
            score = dice_num
        else:
            score *= 2
        if score >= k:
            prob = (1/2)**(i-1)
            break
    return prob

prob_all = 0
for i in range(n):
    prob_all += (get_prob(i+1,k))*(1/n)

print(prob_all)