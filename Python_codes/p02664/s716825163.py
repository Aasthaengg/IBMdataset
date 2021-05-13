def generate_max_PPD_str(T):
  # in any case, it's best to replace "?" with "D"
  return T.replace("?","D")

T = input()
ans = generate_max_PPD_str(T)
print(ans)