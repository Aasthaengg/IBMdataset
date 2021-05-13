import heapq
N,M=map(int,input().split())
A=list(map(int,input().split()))
heapq.heapify(A)
numbers=[]
for _ in range(M):
    B,C=map(int,input().split())
    numbers.append([C,B])
numbers=sorted(numbers,reverse=True)
for number in numbers:
    B=number[1]
    C=number[0]
    for _ in range(B):
        a = heapq.heappop(A)
        if C <= a:
            heapq.heappush(A, a)
            break
        else:
            heapq.heappush(A,C)
print(sum(A))
