# 駐車場があり、以下の二種類のプランのどちらかを選んで駐車できます。 プラン 1 : T 時間駐車した場合、 A × T 円が駐車料金となる。
# プラン 2 : 駐車した時間に関わらず B 円が駐車料金となる。 N 時間駐車するとき、駐車料金は最小でいくらになるか求めてください。

N,A,B = map(int,input().split())

print(min(N * A, B))