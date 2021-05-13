n=int(input())
if n>=2800:
    k=2
elif n>=1200:
    k=1
else:
    k=0
print(['ABC','ARC','AGC'][k])