K = int(input())

#再帰で実装できそう？

memo = set([])

PM = [-1,0,1]

def rec(n):
    if n > 3234566667:
        return
    ichi = n % 10
    for pm in PM:
        if (ichi + pm) != -1 and (ichi + pm) != 10:
            m = n*10 + ichi + pm
            if m not in memo:
                # print(m)
                # if m == 9900:
                #     print(n,ichi + pm)
                memo.add(m)
                rec(m)
    return

for i in range(1,10):
    memo.add(i)
    rec(i)



# rec(9)



memo = list(memo)
memo.sort()

# print(memo[:100])
# print(len(memo))
            
print(memo[K-1])           
            
    
