h,w=map(int, input().split())
new_image=["#"*(w+2)]
for i in range(h):
  new_image.append("#"+input()+"#")
new_image.append("#"*(w+2))
for i in range(h+2):
  print(new_image[i])