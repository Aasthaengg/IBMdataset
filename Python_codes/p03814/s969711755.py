S=input()
print(  abs( min([ k for k,v in enumerate(S) if v == "A" ])  - max([ k for k,v in enumerate(S) if v == "Z" ]) ) +1 )
