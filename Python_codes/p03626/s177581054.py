N=int(input())
S=input()
DIV=1000000007
ans=1
import itertools
wasTate=True
first=True
for key,g in itertools.groupby(S):
  if len(list(g))==1:
    # 縦の場合
    if first:
      # 最初は3通り選べる
      ans=((ans%DIV)*3)%DIV
      first=False
    elif wasTate:
      # ここまで縦だった場合は2通り選べる
      ans=((ans%DIV)*2)%DIV
      wasTate=True
    else:
      # ここまで横だった場合は1通りしかない
      wasTate=True
  else:
    # 横の場合
    if first:
      ans=((ans%DIV)*6)%DIV
      # 最初は6通り選べる
      # 11 11 22 22 33 33
      # 22 33 11 33 11 22
      first=False
      wasTate=False
    elif wasTate:
      # ここまで縦だった場合は2通り選べる
      ans=((ans%DIV)*2)%DIV
      wasTate=False
    else:
      # ここまで横だった場合は3通り選べる
      # 1122 1122 1133
      # 2211 2233 2211
      ans=((ans%DIV)*3)%DIV
      wasTate=False
      
print(ans)