#define k from p
def calck(all_w, p):
    count = 0
    sum = 0
    for w in all_w:
        if sum + w <= p:
            sum += w
        else:
            count+=1 
            sum = w
    return count+1

#get n and k
n, k =map(lambda x: int(x), input().split(' '))

#get all w
#set min and max of p
all_w = []
max = -1
sum = 0
for i in range(n):
    w = int(input())
    all_w.append(w)
    if w > max:
        max = w
    sum += w
max_weight = max
sum_weight = sum
min, max = max, sum
#binary search of p

while min<=max:
    p_pointer = (min+max)//2
    calcedk = calck(all_w, p_pointer)
    if calcedk > k:
        min = p_pointer+1
    elif p_pointer == max_weight or calck(all_w, p_pointer-1) > k:
        print(p_pointer)
        break
    else:
        max = p_pointer-1
