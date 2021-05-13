wt=['Sunny', 'Cloudy', 'Rainy']
s=input()
nxt=(wt.index(s))+1
print(wt[0] if s=='Rainy' else wt[nxt])
