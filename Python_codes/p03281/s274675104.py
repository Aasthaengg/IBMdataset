N = int(input())
p=0
if N < 105:
    print(0)
else:
    for n in range(1,  N+1, 2):
        ans = []
        for i in range(2, int(n**0.5)+1):
            while n % i == 0:
                ans.append(i)
                n //= i
        if n!=1:ans.append(n)

        A = 1
        sp = list(set(ans))
        for s in sp:
            A *= ans.count(s)+1
        if A == 8:
            p+=1

    print(p)