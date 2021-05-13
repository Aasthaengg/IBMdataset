k = int(input())
even = [i for i in range(1, k+1) if i%2==0]
odd = [i for i in range(1, k+1) if i%2!=0]
ans_lst = []
for i in even:    
    for j in odd:
        even_odd = []
        even_odd.append(i)
        even_odd.append(j)
        ans_lst.append(even_odd)
print(len(ans_lst))