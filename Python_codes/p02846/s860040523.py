T1,T2=map(int,input().split())
A1,A2=map(int,input().split())
B1,B2=map(int,input().split())

Adist1=T1*A1
Adist2=T2*A2
Bdist1=T1*B1
Bdist2=T2*B2

# 最初から同じ速度の場合
if Adist1==Bdist1:
  print("infinity")
# Aが先に行ってしまってBが絶対おいつけない場合
elif Adist1>Bdist1 and Adist1+Adist2>Bdist1+Bdist2:
  print(0)
# Bが先に行ってしまってAが絶対おいつけない場合
elif Adist1<Bdist1 and Adist1+Adist2<Bdist1+Bdist2:
  print(0)
# 無限に出会う場合
elif Adist1+Adist2==Bdist1+Bdist2:
  print("infinity")
# 追いついたり追いつかなかったりパターン(Aが先に行く)
elif Adist1>Bdist1 and Adist1+Adist2<Bdist1+Bdist2:
  diff=(Bdist1+Bdist2)-(Adist1+Adist2)
  print(2*((Adist1-Bdist1)//diff)+((Adist1-Bdist1)%diff!=0))
# 追いついたり追いつかなかったりパターン(Bが先に行く)
elif Adist1<Bdist1 and Adist1+Adist2>Bdist1+Bdist2:
  diff=(Adist1+Adist2)-(Bdist1+Bdist2)
  print(2*((Bdist1-Adist1)//diff)+((Bdist1-Adist1)%diff!=0))
