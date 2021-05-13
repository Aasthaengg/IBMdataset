n = int(input())
a = list(map(int, input().split()))
a = [i-idx-1 for idx,i in enumerate(a)]
import statistics as st
b = st.median(a)
print(int(sum([abs(i-b) for i in a])))