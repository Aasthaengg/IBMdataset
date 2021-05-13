N = int(input())
plot = list(map(int,input().split()))
plot.sort(reverse=True)
print(plot[0]-plot[-1])