import re 
T=input() 



T=T.replace("???", "DDD")
T=T.replace("??", "DD")

T=T.replace('D?D', 'DPD')
T=T.replace('D?P', 'DDP')
T=T.replace('P?D', 'PDD')
T=T.replace('P?P', 'PDP')

T=T.replace('?P', 'DP')
T=T.replace('?D', 'PD')

T=T.replace('P?', 'PD')
T=T.replace('D?', 'DD')

T=T.replace('?', 'D')

#T=re.sub("?", "D",T)
#T.replace('P?P', 'PDP')

print(T)