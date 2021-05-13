N = int(input())
print("{:.10f}".format((N//2)/N) if N%2 ==0 else "{:.10f}".format((N//2+1)/N))