# 072b
class Atc_072b:
    def __init__(self, s: str) -> str:
        self.s = s

    def odd(self):
        s_odd = ""
        for i in range(0, len(self.s)):
            if i % 2 == 0:
                s_odd += self.s[i]
        return s_odd


s_input = input()
print(Atc_072b(s_input).odd())
