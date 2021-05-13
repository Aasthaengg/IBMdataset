N = int(input())
T, A = map(int, input().split())
list1 = []
H = list(map(int, input().split()))
X = [abs(T-h*0.006-A) for h in H]
print(X.index(min(X))+1)