al,WA=map(int,input().split())
AC=al-WA

time_per_submit=AC*100+WA*1900
submit_kitaichi=2**WA
print(time_per_submit*submit_kitaichi)