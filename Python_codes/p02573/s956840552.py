import sys
if sys.argv[-1] == 'ONLINE_JUDGE':
    import os, zlib, base64
    open('solve.pyx', 'wb').write(zlib.decompress(base64.b85decode("c${TYO>cuR480@qAH2g<SksD5J4|Tok8~W85Fi=^lxC{7Uq74hU0=X{&(AMTO53&2Xd%xxXSJz7>bCE!gI2XS<-(vOg8X%LXU;vhylGT3lX}ZdrAE@IQs{2RE9GR(EkmL<t_%ZNs1oq^`kGMW(1(Ga6!i>F7X}`H7r5y^)s+#F<9Kdtv{BTL6HF9?=_=i%VE`DDGzbO~GDv*+Uh77|Wh7Au1V>|0yp(l`$OpW=ry#82-wQ%&5*=L<I3nkS91mLMeyjnxoC_Mo3uVbQ@U1`8@2@<^5lK3Aat{slZ0e;f-VC71YKCFZGT@9(su?&&4({63n|X#@)0TYNZqu@}piynS!l;c`8{%8;w6tA`FP1qj<+5Xskk~=E1`badh}FFHdOq<Z@*POwP?JBF$%S|<lLNOc5Aw%s(BC5>_v-Un{8mi7T;8d_YO*KO;Xw>(82E=B9iEFXbHIzhll}vB`qr2")))
    os.system('cythonize -i -3 -b solve.pyx')
import solve