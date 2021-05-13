ans={'1','2','3'}
a,b=input(),input()
print(*(ans-set([a,b])))